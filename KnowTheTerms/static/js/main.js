document.addEventListener("DOMContentLoaded", () => {
  const termsOfServiceInput = document.getElementById("terms_of_service_input");
  const submitButton = document.getElementById("submit_button");
  const summaryOutput = document.getElementById("summary_output");
  const safetyRemarkOutput = document.getElementById("safety_remark_output");

  submitButton.addEventListener("click", async () => {
    const termsOfServiceUrl = termsOfServiceInput.value;
    if (!termsOfServiceUrl) {
      alert("Please enter a Terms of Service URL.");
      return;
    }

    submitButton.disabled = true;
    const response = await fetch("/summarize", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ terms_of_service_url: termsOfServiceUrl }),
    });

    if (response.ok) {
      const data = await response.json();
      displayResults(data.summary, data.safety_remark);
    } else {
      alert("An error occurred. Please try again.");
    }

    submitButton.disabled = false;
  });

  function displayResults(summary, safetyRemark) {
    summaryOutput.textContent = summary;
    safetyRemarkOutput.textContent = safetyRemark;
  }
});