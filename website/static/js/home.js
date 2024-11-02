// VogueX
// Copyright (c) 2024 Group 84: Gokul Prakash Ramesh, Haricharan Bharathi, Raghunandan Ganesh Mante
// This project is licensed under the MIT License.
// #
// Governance Model:
// This project follows an open governance model, which includes a leadership team,
// contribution guidelines, a code of conduct, and a clear decision-making process.
// Contributions are welcome, and please see CONTRIBUTING.md for details.

var formattedFormData = {};
$(document).ready(function(){
    $(".recoButton1").click(function(e){
        var formData = $('#recoForm').serializeArray();
        
        for(var i = 0; i < formData.length; i++){
            formattedFormData[formData[i]["name"]] = formData[i]["value"];
        }
        console.log(formattedFormData);
        formData = JSON.stringify(formattedFormData)
        var occasionValue=formattedFormData["occasion"];
        var cityValue=formattedFormData["city"]
        localStorage.setItem("occasionVal",occasionValue);
        localStorage.setItem("cityVal",cityValue);
        // console.log(occasionVal)
        // console.log(cityVal)
        console.log(formData);
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/newrecommendations",
            data: JSON.stringify(formattedFormData),
            success: function(data){
                // Convert image paths to a format that can be sent in the URL
                var imagePaths = data["images"].map(encodeURIComponent).join(',');
                
                // Redirect to results.html with image paths in URL query
                var redirectUrl = `${window.location.protocol}//${window.location.host}/results?images=${imagePaths}`;
                location.href = redirectUrl;
            },
            dataType: "json",
            contentType: "application/json"
        });        
        // $.ajax({
        //     type: "POST",
        //     url: "/recommendations",
        //     data: formData,
        //     success: function(data){
                
        //         var str = "";
        //         for(var i = 0; i < data["links"].length; i++){
        //             str += data["links"][i] + " || ";
        //         }
        //         console.log(data["links"]);
        //         var redirectUrl = window.location.protocol + "//" + window.location.host + "/results?" + str;
        //         location.href = redirectUrl;
        //     },
        //     dataType: "json",
        //     contentType : "application/json"
        // });
        formData = JSON.stringify(formattedFormData)
        // $.ajax({
        //     type:"POST",
        //     url:"/favourites",
        //     data:formData,
        //     success:function(){
        //         console.log("success");
        //     },
        //     dataType: "json",
        //     contentType : "application/json"
        // })
    });
    $(".recoButton1").click(function(e){
        var loader= document.getElementById( 'center' )
        loader.style.display = '';
    });
});

