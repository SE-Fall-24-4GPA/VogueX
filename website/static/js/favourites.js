var formattedFormData2={};
$(document).ready(function(){
    $('button').click(function(e){

    let buttonId=this.id;
    let imgsrc=document.getElementById(buttonId).src;
    formattedFormData2["favouriteUrl"]=imgsrc
    formData = JSON.stringify(formattedFormData2)
    //console.log(formData)
    e.preventDefault();
		$.ajax({
			type:"POST",
            url:"/favourites",
            data:formData,
            success:function(response){
                var redirectUrl = window.location.protocol + "//" + window.location.host + "/favourites";
                location.href = redirectUrl;
                
            },
			dataType: "json",
            contentType : "application/json"
		})
    })

})