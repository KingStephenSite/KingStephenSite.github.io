const axios = require('axios');

const promptInput = document.getElementById("prompt");
const generateButton = document.getElementById("generate-button");
const lyricsContainer = document.getElementById("lyrics");
const responseContainer = document.getElementById("response-container");
const response = document.getElementById("response");

generateButton.addEventListener("click", async function() {
  const prompt = promptInput.value;
  try {
    const response = await axios.post('https://api.openai.com/v1/engines/davinci/completions', {
      prompt: prompt,
      max_tokens: 100,
      api_key: "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"
    });

    const rapLyric = response.data.choices[0].text;
    lyricsContainer.innerHTML = `<p> ${rapLyric}</p>`;
    responseContainer.style.display = "block";
    response.innerText = "API response: " + JSON.stringify(response.data);
  } catch (error) {
    console.error(error);
    responseContainer.style.display = "block";
    window.alert = "Error: " + error;
  }
});