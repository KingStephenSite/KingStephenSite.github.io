const axios = require('axios');
const responseContainer = document.getElementById("response-container");
const response = document.getElementById("response");

responseContainer.style.display = "block";
response.innerText = "API response: " + JSON.stringify(apiResponse);


async function generateRapLyric() {
  const prompt = "Write a rap about technology";

  try {
    const response = await axios.post('https://api.openai.com/v1/engines/davinci/completions', {
      prompt: prompt,
      max_tokens: 100,
      api_key: "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"
    });

    const rapLyric = response.data.choices[0].text;
    console.log(rapLyric);
  } catch (error) {
    console.error(error);
  }
}

generateRapLyric();