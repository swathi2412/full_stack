async function loadUser(){
    let userId = document.getElementById("userId").value;
    let res = await fetch(`http://127.0.0.1:5000/recommend/${userId}`);
    let data = await res.json();

    document.getElementById("profile").innerHTML = `
        <p class="small">User #${userId} | Personalized recommendations based on similar users</p>
    `;

    let html="";
    data.recommendations.forEach(r=>{
        html+=`
        <div class="reco">
            <b>Product:</b> ${r.product}<br>
            <span class="small">${r.why}</span>
        </div>`;
    });

    document.getElementById("recommendations").innerHTML=html;
}

async function search(){
    let q=document.getElementById("query").value;
    let res=await fetch(`http://127.0.0.1:5000/query?q=${q}`);
    let data=await res.json();

    let html=`<b>Understood:</b> ${JSON.stringify(data.understood)}<br><br>`;

    data.results.forEach(r=>{
        html+=`
        <div class="reco">
            <b>${r.product}</b><br>
            <span class="small">${r.why}</span>
        </div>`;
    });

    document.getElementById("searchResults").innerHTML=html;
}

async function coldStart(){
    let res=await fetch(`http://127.0.0.1:5000/coldstart`);
    let data=await res.json();

    let html="";
    data.recommendations.forEach(p=>{
        html+=`<div class="reco">${p}</div>`;
    });

    document.getElementById("cold").innerHTML=html;
}
