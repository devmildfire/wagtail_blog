// скрипт срабатывает на прогрузку страницы и на изменения размеров страницы
// он находит все переполняемые строки тэгов в карточках тэгов и перемещает 
// элементы, которые переполняют строку тэгов, в тултип

function checkOverflow(el)
{
   var curOverflow = el.style.overflow;

   if ( !curOverflow || curOverflow === "visible" )
      el.style.overflow = "hidden";

   var isOverflowing = el.clientWidth < el.scrollWidth 
      || el.clientHeight < el.scrollHeight;

   el.style.overflow = curOverflow;

   return isOverflowing;
}

const divList = document.querySelectorAll(".card_tag_div");


for (const [index, element] of divList.entries()) {
    console.log({index, element});
    console.log(`${element} overflow: ${checkOverflow(element)}`);

    // if (checkOverflow(element)) {
    //     let tagList = element.children;
    //     let lastTag = tagList[tagList.length - 2]
    //     let text = lastTag.innerText;
    //     console.log(`${element} has last tag of: `, {text});

    //     console.log(`removing ${element}'s last tag `);
    //     element.removeChild(lastTag);
    //     let resultingTagList = element.children;
    //     console.log(`now ${element}'s taglist is ... `, {resultingTagList});

    //     let tagWithTooltip = resultingTagList[resultingTagList.length - 1];
    //     console.log(`tagWithTooltip is ... `, {tagWithTooltip});
        

    //     let Tooltip = tagWithTooltip.children[tagWithTooltip.children.length - 1];
    //     console.log(`Tooltip div is ... `, {Tooltip});

    //     Tooltip.appendChild(lastTag);
    //     console.log(`Added ${text} tag to Tooltip `, {Tooltip});
        
    // }

    console.log(`BEFORE CYCLE ${element} has oferflow == ${checkOverflow(element)}`);

    while (element.children.length > 2 && checkOverflow(element)  ) {

        console.log(`${element} has children list with length of ${element.children.length}`);

        console.log(`${element} has oferflow == ${checkOverflow(element)}`);
        

        let tagList = element.children;
        let lastTag = tagList[tagList.length - 2]
        let text = lastTag.innerText;
        console.log(`${element} has last tag of: `, {text});

        console.log(`removing ${element}'s last tag `);
        element.removeChild(lastTag);
        let resultingTagList = element.children;
        console.log(`now ${element}'s taglist is ... `, {resultingTagList});

        let tagWithTooltip = resultingTagList[resultingTagList.length - 1];
        console.log(`tagWithTooltip is ... `, {tagWithTooltip});
        

        let Tooltip = tagWithTooltip.children[tagWithTooltip.children.length - 1];
        console.log(`Tooltip div is ... `, {Tooltip});

        Tooltip.appendChild(lastTag);
        console.log(`Added ${text} tag to Tooltip `, {Tooltip});
        
    }


    console.log({element}, ` overflow is presumably: ${checkOverflow(element)} at last`)
}
