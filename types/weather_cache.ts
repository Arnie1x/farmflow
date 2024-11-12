import axios from 'axios';

interface WeatherData {
  location: { longitude: number; latitude: number };
  forecast_data: any; // assuming JSON format
  updated_at: Date;
}

class WeatherCache {
  private openWeatherMapApiKey: string;

  constructor(openWeatherMapApiKey: string) {
    this.openWeatherMapApiKey = openWeatherMapApiKey;
  }

  async getWeatherData(location: { longitude: number; latitude: number }): Promise<WeatherData | null> {
    const client = useSupabaseClient();
    const { data, error } = await client
      .from('weather')
      .select('*')
      .eq('location', JSON.stringify(location));

    if (error) {
      throw error;
    }

    if (data.length > 0) {
      return data[0];
    }

    const openWeatherMapResponse = await axios.get(`https://api.openweathermap.org/data/3.0/onecall`, {
      params: {
        lat: location.latitude,
        lon: location.longitude,
        units: 'metric',
        appid: this.openWeatherMapApiKey,
        exclude: 'minutely,daily,alerts'
      },
    });

    const forecastData = openWeatherMapResponse.data;
    const weatherData: WeatherData = {
      location,
      forecast_data: forecastData,
      updated_at: new Date()
    };

    const { error: insertError } = await client
      .from('weather')
      .upsert([weatherData]);

    if (insertError) {
      throw insertError;
    }

    return weatherData;
  }
}

export default WeatherCache;