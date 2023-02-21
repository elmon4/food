function weitereZutat(){
    console.log("button clicked");
    const form = document.createElement("div");
    form.className = "input-group";
    const span = document.createElement("span");
    span.className = "input-group-text";

    const input1 = document.createElement("input");
    input1.type = "text";
    input1.setAttribute("aria-label", "Zutat");
    input1.className = "form-control";
    input1.placeholder = "Zutat";
    input1.id = "zutat";

    const input2 = document.createElement("input");
    input2.type = "text";
    input2.setAttribute("aria-label", "Menge");
    input2.className = "form-control";
    input2.placeholder = "Menge in g";
    input2.id = "Menge in g";

    form.appendChild(span);
    form.appendChild(input1);
    form.appendChild(input2);

    const container = document.getElementById("form-container");
    container.appendChild(form);
}