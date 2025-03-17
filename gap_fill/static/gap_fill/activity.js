function getCookie(name) {
    // function provided by Django docs
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const check_url = document.getElementById("check-url").getAttribute("url")
const option_elems = document.getElementsByClassName("drop-item");

async function check_input() {
    option_arr = Array.from(option_elems);
    json = {};
    option_arr.forEach(elem => {
            // add option id, slot number pairs to json
            json[elem.id.replace("option-", "")] = elem.parentNode.id.replace("slot-", "");
        }
    );
    // configure and make input checking request to backend
    const request = new Request(
        check_url, {
            method: "POST",
            credentials: "same-origin",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: JSON.stringify(json),
        }
    );
    const rsp = await fetch(request)
    const results = await rsp.json();
    Object.keys(results).forEach(slot_num => {
        console.log(document.getElementById("slot-"+slot_num));
        option = document.getElementById("slot-"+slot_num).firstChild;
        if (results[slot_num] === true) {
            // if slot contains correct option, mark option as correct and disable its drag and drop
            option.setAttribute("draggable", "false")
            option.classList.remove("drop-item")
            option.classList.add("correct-option")
        }

    })
}
    
