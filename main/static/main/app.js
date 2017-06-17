/**
 * Created by aqali on 6/14/17.
 */

window.onload = function () {
    $(".like").on("click", function(e) {
       e.preventDefault();
       $.post(this.href, function(data) {

       });
    });
};
