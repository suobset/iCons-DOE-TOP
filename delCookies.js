// DelCookies Written by Kush S.
// More Info Here: https://skushagra.com/docs/finechive/scripting-shenanigans#delcookies

(function() {
    // Get all cookies
    var allCookies = document.cookie.split("; ");
    for (var cookieIndex = 0; cookieIndex < allCookies.length; cookieIndex++) {
        // Split cookie into key-value pair
        var cookieParts = allCookies[cookieIndex].split("=");
        var cookieName = encodeURIComponent(cookieParts[0]);
        var cookieValue = cookieParts[1];
        // Split hostname into domain parts
        var domainParts = window.location.hostname.split(".");
        // Iterate over domain parts
        while (domainParts.length > 0) {
            // Build cookie base for deletion
            var cookieBase = cookieName + '=; expires=Thu, 01-Jan-1970 00:00:01 GMT; domain=' + domainParts.join('.') + '; path=';
            var pathParts = location.pathname.split('/');
            document.cookie = cookieBase + '/';
            // Iterate over path parts
            while (pathParts.length > 0) {
                document.cookie = cookieBase + pathParts.join('/');
                pathParts.pop();
            }
            domainParts.shift();
        }
    }
})();