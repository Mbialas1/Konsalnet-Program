function ChangeInputAdd(Name)
{
    
    var City = document.getElementById('City');
    var RamSpec = document.getElementById('RamSpec');
    
    if (Name == "City")
    { 
        City.style.display = 'block';
        RamSpec.style.display = 'none';
        var UnSetRequired = RamSpec.children;
        var UnSetRequiredTarget = City.children;
        UnSetRequired[1].removeAttribute("required");
        UnSetRequired[3].removeAttribute("required");
        UnSetRequired[1].value = "";
        UnSetRequired[3].value = "";
        UnSetRequiredTarget[1].setAttribute("required","true");
        UnSetRequiredTarget[3].setAttribute("required","true");
    }
    else
    {
        var UnSetRequiredTarget = RamSpec.children;
        var UnSetRequired = City.children;
        UnSetRequired[1].removeAttribute("required");
        UnSetRequired[3].removeAttribute("required");
        UnSetRequired[1].value = "";
        UnSetRequired[3].value = "";
        UnSetRequiredTarget[1].setAttribute("required","true");
        UnSetRequiredTarget[3].setAttribute("required","true");
        RamSpec.style.display = 'block';
        City.style.display = 'none';
    }
}

function CheckBoxGet()
{
    var City = document.getElementById('City').style.display;
    if(City == 'none')
    {
       var CityTextBox = document.getElementById('RamSpec').children;
       if(CityTextBox[1].value === "")
       {
           alert("To pole nie może pozostać puste. - Komputer");
           return false;
       }
       if(CityTextBox[3].value === "")
       {
           alert("To pole nie może pozostać puste. - RAM");
           return false;
       }
    }
    else
    {
        alert("miasto");
    }
}

function CheckBoxMeters(thisa)
{
    if(thisa.checked == true)
    {
        document.getElementById("buttonToolbarKm").value = "Klop";
        TakeTargetToMap();
    }
}

