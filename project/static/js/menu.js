function linktoselftest() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            location.href = "selftest";
        }
    };
    xhttp.open('GET', 'selftest');
    xhttp.send();
};

function linktosignup() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            location.href = "signup";
        }
    };
    xhttp.open('GET', 'signup');
    xhttp.send();
};

function linktosearch() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            location.href = "search";
        }
    };
    xhttp.open('GET', 'search');
    xhttp.send();
};

function linktohome() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            location.href = "/";
        }
    };
    xhttp.open('GET', '/');
    xhttp.send();
};