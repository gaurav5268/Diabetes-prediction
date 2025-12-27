function getValue(id){

    let val = document.getElementById(id).value;

    if(val === "" || val === null){
        throw "Please fill all fields";
    }

    if(val.includes("+")) return 4;

    return parseFloat(val);
}


async function predict(){

    try{

        let data = {
            Pregnancies: getValue("Pregnancies"),
            Glucose: getValue("Glucose"),
            BloodPressure: getValue("BloodPressure"),
            SkinThickness: getValue("SkinThickness"),
            Insulin: getValue("Insulin"),
            BMI: getValue("BMI"),
            DiabetesPedigreeFunction: getValue("DiabetesPedigreeFunction"),
            Age: getValue("Age")
        };

        document.getElementById("result").innerHTML =
            "<span class='ok'>⏳ Predicting...</span>";

        let res = await fetch("/predict", {
            method:"POST",
            headers:{ "Content-Type":"application/json" },
            body:JSON.stringify(data)
        });

        let resJson = await res.json();

        if(resJson.error){
            document.getElementById("result").innerHTML =
                "<span class='warn'>❌ " + resJson.error + "</span>";
            return;
        }

        document.getElementById("result").innerHTML =
            resJson.prediction === 1
            ? "<span class='warn'>⚠ High Diabetes Risk</span>"
            : "<span class='ok'>✔ Low Diabetes Risk</span>";

    }
    catch(err){

        document.getElementById("result").innerHTML =
        "<span class='warn'>❌ " + err + "</span>";
    }

}
