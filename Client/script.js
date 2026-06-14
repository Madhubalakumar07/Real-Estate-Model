function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");

    for (var i = 0; i < uiBathrooms.length; i++) {
        if (uiBathrooms[i].checked) {
            return parseInt(uiBathrooms[i].value);
        }
    }
    return -1;
}

function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");

    for (var i = 0; i < uiBHK.length; i++) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1;
}

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");

    var sqft = document.getElementById("uiSqft").value;
    var bhk = getBHKValue();
    var bath = getBathValue();
    var location = document.getElementById("uiLocations").value;
    var estPrice = document.getElementById("uiEstimatedPrice");

    $.ajax({
        url: "http://127.0.0.1:5000/predict_price",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({
            location: location,
            sqft: sqft,
            bath: bath,
            bhk: bhk
        }),
        success: function(data) {
            console.log(data);
            estPrice.innerHTML =
                "<h2>" + data.estimated_price.toString() + " Lakhs</h2>";
        },
        error: function(xhr, status, error) {
            console.error(error);
            estPrice.innerHTML =
                "<h2>Error predicting price</h2>";
        }
    });
}

function onPageLoad() {
    console.log("document loaded");

    $.get("http://127.0.0.1:5000/get_location_names", function(data) {

        if (data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");

            $('#uiLocations').empty();

            for (var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
}

window.onload = onPageLoad;