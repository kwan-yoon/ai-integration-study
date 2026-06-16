import axios from "axios";

const BASE_URL = "http://localhost:8000";

export const sendMessage = async (message: string) => {
  const response = await axios.post(`${BASE_URL}/chat`, { message });
  return response.data.reply;
};

export const summarizeText = async (text: string) => {
  const response = await axios.post(`${BASE_URL}/summarize`, { text });
  return response.data.summary;
};
