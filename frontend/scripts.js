document.getElementById("churnForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const contract = document.getElementById("contract").value;
    const internet = document.getElementById("internet").value;

    // Prepare data in model-required format
    const data = {
        tenure: parseInt(document.getElementById("tenure").value),
        MonthlyCharges: parseFloat(document.getElementById("monthlyCharges").value),
        TotalCharges: parseFloat(document.getElementById("totalCharges").value),

        gender_Male: 1,
        SeniorCitizen: 0,
        Partner_Yes: 1,
        Dependents_Yes: 0,
        PhoneService_Yes: 1,
        MultipleLines_Yes: 0,
        InternetService_Fiber_optic: internet === "fiber" ? 1 : 0,
        OnlineSecurity_Yes: 0,
        OnlineBackup_Yes: 1,
        DeviceProtection_Yes: 0,
        TechSupport_Yes: 0,
        StreamingTV_Yes: 1,
        StreamingMovies_Yes: 1,
        Contract_One_year: contract === "one" ? 1 : 0,
        Contract_Two_year: contract === "two" ? 1 : 0,
        PaperlessBilling_Yes: 1,
        PaymentMethod_Electronic_check: 1
    };

    const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    const probability = result.churn_probability;
    let risk = "Low";
    let className = "low";

    if (probability >= 0.6) {
        risk = "High";
        className = "high";
    } else if (probability >= 0.3) {
        risk = "Medium";
        className = "medium";
    }

    const box = document.getElementById("resultBox");
    box.className = `result-box ${className}`;

    document.getElementById("predictionText").innerText =
        result.churn_prediction === 1
            ? "Prediction: Customer is likely to churn"
            : "Prediction: Customer is not likely to churn";

    document.getElementById("probabilityText").innerText =
        `Churn Probability: ${(probability * 100).toFixed(2)}%`;

    document.getElementById("riskText").innerText =
        `Risk Level: ${risk}`;

    box.classList.remove("hidden");

});
console.log("script.js loaded");

document.getElementById("churnForm").addEventListener("submit", async function (e) {
    e.preventDefault();
    console.log("Predict button clicked");

    const contract = document.getElementById("contract").value;
    const internet = document.getElementById("internet").value;

    // DATA SENT TO BACKEND
    const data = {
        tenure: parseInt(document.getElementById("tenure").value),
        MonthlyCharges: parseFloat(document.getElementById("monthlyCharges").value),
        TotalCharges: parseFloat(document.getElementById("totalCharges").value),

        gender_Male: 1,
        SeniorCitizen: 0,
        Partner_Yes: 1,
        Dependents_Yes: 0,
        PhoneService_Yes: 1,
        MultipleLines_Yes: 0,
        InternetService_Fiber_optic: internet === "fiber" ? 1 : 0,
        OnlineSecurity_Yes: 0,
        OnlineBackup_Yes: 1,
        DeviceProtection_Yes: 0,
        TechSupport_Yes: 0,
        StreamingTV_Yes: 1,
        StreamingMovies_Yes: 1,
        Contract_One_year: contract === "one" ? 1 : 0,
        Contract_Two_year: contract === "two" ? 1 : 0,
        PaperlessBilling_Yes: 1,
        PaymentMethod_Electronic_check: 1
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        console.log("Backend result:", result);

        // SHOW RESULT
        document.getElementById("predictionText").innerText =
            result.churn_prediction === 1
                ? "Prediction: Customer is likely to churn"
                : "Prediction: Customer is not likely to churn";

        document.getElementById("probabilityText").innerText =
            `Churn Probability: ${(result.churn_probability * 100).toFixed(2)}%`;

        let risk = "Low";
        if (result.churn_probability >= 0.6) risk = "High";
        else if (result.churn_probability >= 0.3) risk = "Medium";

        document.getElementById("riskText").innerText =
            `Risk Level: ${risk}`;

        document.getElementById("resultBox").classList.remove("hidden");

    } catch (error) {
        console.error("Error:", error);
    }
});
