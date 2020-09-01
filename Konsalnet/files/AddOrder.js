var NumberSlot = 2;
var TextToMail = "";
var IloscSztuk = 1;
const Url = 'http://127.0.0.1:8000/AddRam.html/'

function PlusButton()
{
   var TitleSlot = document.getElementById('ToolbarTextBox');
   var TitleSlotParent = TitleSlot.children[2];
   
   var nodeP = document.createElement("p");
   TitleSlotParent.children[0].innerHTML = "#" + NumberSlot.toString();
   var node = TitleSlotParent.cloneNode(true);
   TitleSlotParent.children[0].innerHTML = "#1";

   TitleSlot.appendChild(nodeP);
   node.children[1].name = "ChoiceFieldComputer"+NumberSlot.toString();
   node.children[2].name = "GB"+NumberSlot.toString();
   node.children[3].name = "NrStack"+NumberSlot.toString();
   node.children[4].value = NumberSlot.toString();
   TitleSlot.appendChild(node);
   NumberSlot++;
   IloscSztuk++;
   var ChangeHelpForDjango = document.getElementById('NrSztuk');
   ChangeHelpForDjango.innerHTML = IloscSztuk.toString();
}

function MinusButton()
{
    var TitleSlot = document.getElementById('ToolbarTextBox');
    if(TitleSlot.children.length > 3)
    {
    var TitleSlotLastParen = TitleSlot.children[TitleSlot.children.length-1];
    var TitleSlotLastParenP = TitleSlot.children[TitleSlot.children.length-2];

    TitleSlotLastParen.parentNode.removeChild(TitleSlotLastParen);
    TitleSlotLastParenP.parentNode.removeChild(TitleSlotLastParenP);
    NumberSlot--;
    IloscSztuk--;
   var ChangeHelpForDjango = document.getElementById('NrSztuk');
   ChangeHelpForDjango.innerHTML = IloscSztuk.toString();
    }
}

function SendOrderTo()
{
    var TitleSlot = document.getElementById('ToolbarTextBox');
    var NumberSlotChild = TitleSlot.children.length / 2 - 0.5;

    var JsonFile = {};
    var Child;
    var ChildNr = 2;
    var ListRepeatObjects = [];
    for(i=0;i<NumberSlotChild;i++)
    {
        Child = TitleSlot.children[ChildNr].children[1].value;
        for(j=0;j<ListRepeatObjects.length;j++)
        {
            if(Child === ListRepeatObjects[j])
            {
                alert("Jakiś model się powtarza.");
                return;
            }
        }
        var RamChild = TitleSlot.children[ChildNr].children[2].value;
        var SizeChild = TitleSlot.children[ChildNr].children[3].value;
        JsonFile[Child] = RamChild + "GB," + SizeChild;
        ChildNr += 2;
        ListRepeatObjects[i] = Child;
    }

    const JsonText = JSON.stringify(JsonFile);

    $.ajax({
        type: 'POST',
        url:'{% url "create" %}',
        traditional: true,
        dataType: 'html',
        success: function(result){
            $('#AddRam.html').append(result);
            },
        error: function()
        {
          //  alert("Błąd w pliku AddOrder.js ~ Ajax problem!");
        }
    });
  
}