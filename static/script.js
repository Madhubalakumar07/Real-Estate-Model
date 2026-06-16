function getBathValue() {
    let uiBathrooms = document.getElementsByName("uiBathrooms");
    for (let i = 0; i < uiBathrooms.length; i++) {
        if (uiBathrooms[i].checked) {
            return parseInt(uiBathrooms[i].value);
        }
    }
    return -1;
}
function getBHKValue() {
    let uiBHK = document.getElementsByName("uiBHK");

    for (let i = 0; i < uiBHK.length; i++) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1;
}
function onClickedEstimatePrice() {

    console.log("Estimate price button clicked");

    let sqft = document.getElementById("uiSqft").value;

    let bhk = getBHKValue();

    let bath = getBathValue();

    let location = document.getElementById("uiLocations").value;

    let estPrice = document.getElementById("uiEstimatedPrice");
    $.ajax({

        url: "/predict_price",

        type: "POST",

        contentType: "application/json",

        data: JSON.stringify({

            location: location,

            sqft: sqft,

            bath: bath,
            bhk: bhk
        }),
        success: function (data) {
            console.log(data);
            estPrice.innerHTML =
                "<h2>" + data.estimated_price + " Lakhs</h2>";
        },
        error: function (xhr, status, error) {
            console.log(xhr);
            console.log(status);
            console.log(error);
            estPrice.innerHTML =
                "<h2>Error predicting price</h2>";
        }
    });
}
function onPageLoad() {
    console.log("Document loaded");
    $.get("/get_location_names", function (data) {
        if (data) {
            let locations = data.locations;
            let uiLocations =
                document.getElementById("uiLocations");

            $("#uiLocations").empty();
            $("#uiLocations").append(
                new Option(
                    "Choose a Location",
                    ""
                )
            );
            for (let i in locations) {
                let opt =
                    new Option(
                        locations[i],
                        locations[i]
                    );
                $("#uiLocations")
                    .append(opt);
            }
        }
    });
}
window.onload = onPageLoad;