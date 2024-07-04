require("dotenv").config();
const express = require("express");
const axios = require("axios");

const app = express();
const port = process.env.PORT || 80;
const apiKey = process.env.API_KEY;

app.set("view engine", "ejs");
app.use(express.static("public"));

app.get("/", (req, res) => {
  res.render("index");
});

app.get("/convert", async (req, res) => {
  const { amount, from, to } = req.query;
  console.log("Hello");
  const date = "2024-07-02";

  const options = {
    method: "GET",
    url: "https://api.currencyapi.com/v3/historical",
    params: { apikey: apiKey, base_currency: from, currencies: to, date },
  };

  try {
    const response = await axios.request(options);
    res.json({ convertedAmount: response.data.data[to].value * amount });
  } catch (error) {
    console.log(error);
    res.status(500).send("Error converting currency");
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
