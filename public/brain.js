document.querySelector(".convert").addEventListener("click", async function () {
  const amount = document.querySelector(".search-amount-bar").value;
  const from = document.querySelector(".from").value;
  const to = document.querySelector(".to").value;

  try {
    const response = await fetch(
      `/convert?amount=${amount}&from=${from}&to=${to}`
    );
    const data = await response.json();
    document.querySelector(
      ".res"
    ).textContent = `Converted Amount: ${data.convertedAmount}`;
  } catch (error) {
    document.querySelector(".res").textContent = "Error converting currency";
  }
});
