import axios from 'axios';

interface WeatherData {
  location: { longitude: number; latitude: number };
  forecast_data: any; // assuming JSON format
  expires_at: Date;
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
      const weatherData = data[0];
      if (weatherData.expires_at > new Date()) {
        return weatherData;
      }
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
      expires_at: new Date(Date.now() + 6 * 60 * 60 * 1000), // 6 hours from now
    };

    const {error: deleteError} = await client
      .from('weather')
      .delete()
      .eq('location', JSON.stringify(location));

    if (deleteError) {
      throw deleteError;
    }

    const { error: insertError } = await client
      .from('weather')
      .insert([weatherData]);

    if (insertError) {
      throw insertError;
    }

    return weatherData;
  }
}

export default WeatherCache;