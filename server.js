require("dotenv").config();
const express = require("express");
const axios = require("axios");

const app = express();
const port = process.env.PORT || 3000;
const apiKey = process.env.API_KEY;

app.set("view engine", "ejs");
app.use(express.static("public"));

app.get("/", (req, res) => {
  res.render("index");
});

app.get("/convert", async (req, res) => {
  const { amount, from, to } = req.query;

  const options = {
    method: "GET",
    url: "https://api.apilayer.com/exchangerates_data/convert",
    params: { to, from, amount },
    headers: {
      apikey: apiKey,
    },
  };

  try {
    const response = await axios.request(options);
    res.json({ convertedAmount: response.data.result });
  } catch (error) {
    res.status(500).send("Error converting currency");
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
