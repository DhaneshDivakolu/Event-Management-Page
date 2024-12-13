const navd = document.getElementsByTagName("li");
const d = document.getElementById("dp");
const dh = document.getElementsByTagName("input");
const dha = document.getElementsByTagName("button");

for(let l=0; l<navd.length; l++)
{
    const ele = navd[l];
    ele.addEventListener("mouseenter",function(){
        ele.style.boxShadow ="10px 10px 70px aliceblue";
    })
    ele.addEventListener("mouseleave",function(){
        ele.style.boxShadow ="";
    })
}

d.addEventListener("mouseenter",function(){
    d.style.color = "yellow";
})
d.addEventListener("mouseleave",function(){
    d.style.color = "";
})

for(let l=0; l<dh.length; l++)
    {
        const ele = dh[l];
        ele.addEventListener("mouseenter",function(){
            ele.style.backgroundColor = "gray";
            ele.style.fontSize = "50px";
        })
        ele.addEventListener("mouseleave",function(){
            ele.style.backgroundColor ="";
            ele.style.fontSize = "";
        })
}

for(let b=0; b<dha.length; b++)
{
    const ele = dha[b];
    ele.addEventListener("mouseenter",function(){
        ele.style.boxShadow ="10px 10px 80px yellow";
    })
    ele.addEventListener("mouseleave",function(){
        ele.style.boxShadow ="";
    })
    ele.addEventListener("click",function(){
        alert('Registered :) ');
    })
}