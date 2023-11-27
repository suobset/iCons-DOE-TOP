document.addEventListener("DOMContentLoaded", function () {
    // Select the navigation bar, open icon, and close icon from the HTML and store in variables
    const menuIcon = document.getElementById("open-icon");
    const navBar = document.querySelector(".menu-items");
    const closeIcon = document.getElementById("close-icon");

    // Add event listeners to close the menu icon, display the close icon and the
    // navbar when the user clicks to open the menu
    menuIcon.addEventListener("click", () => {
        // Toggle the "open" class on the navigation bar to show it
        navBar.classList.toggle("open");

        // Hide the menu icon and display the close icon
        menuIcon.style.display = "none";
        closeIcon.style.display = "block";
    });

    // Add event listener to close the menu on click of the close icon
    closeIcon.addEventListener("click", () => {
        // Remove the "open" class from the navigation bar to hide it
        navBar.classList.remove("open");

        // Display the menu icon and hide the close icon
        menuIcon.style.display = "flex";
        closeIcon.style.display = "none";
    });
});

