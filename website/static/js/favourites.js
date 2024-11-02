// VogueX
// Copyright (c) 2024 Group 84: Gokul Prakash Ramesh, Haricharan Bharathi, Raghunandan Ganesh Mante
// This project is licensed under the MIT License.
// #
// Governance Model:
// This project follows an open governance model, which includes a leadership team,
// contribution guidelines, a code of conduct, and a clear decision-making process.
// Contributions are welcome, and please see CONTRIBUTING.md for details.

var formattedFormData2={};
$(document).ready(
function(){$('button').click(function(e){

    let buttonId=this.id;
    let imgsrc=document.getElementById(buttonId).src;
    formattedFormData2["favouriteUrl"]=imgsrc
    formData = JSON.stringify(formattedFormData2)
    console.log(formData)
    e.preventDefault();
		$.ajax({
			type:"POST",
            url:"/favourites",
            data:formData,
            success:function(response){
               $("#fav_msg").text("Favourite Added Successfully!");
                setTimeout(function() {
                    $("#fav_msg").text("");
                }, 1000);
                
                // Optionally redirect:
                // window.location.href = `/favourites/${userid}`;
            },
            error: function(xhr, status, error) {
                console.error("Error adding favourite:", error);
                $("#fav_msg").text("Error adding favourite. Please try again.");
            },
            dataType: "json",
            contentType: "application/json"
		})
    })

})
function deleteFavourite(favouriteUrl, userId) {
    fetch('/favourites/', {
        method: 'DELETE',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ 'favourite_url': favouriteUrl })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            // Redirect to /favourites/userid using GET
            window.location.href = `/favourites/`;
        } else if (data.error) {
            alert(data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while deleting the favourite');
    });
}

// Add event listeners to dynamically call deleteFavourite
$(document).on('click', 'button.delete-favourite', function(e) {
    e.preventDefault();
    let favouriteUrl = $(this).closest('.media-element').find('img').attr('src');
    let userId = $(this).data('userid');
    deleteFavourite(favouriteUrl, userId);
});