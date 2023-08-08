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

function getElementContentWidth(element) {
   var styles = window.getComputedStyle(element);
   var padding = parseFloat(styles.paddingLeft) +
   parseFloat(styles.paddingRight);
   
   return element.clientWidth - padding;
}


const card_div = document.querySelector(".card_div");
console.log(`Card Div `,{card_div}, ` width == ${getElementContentWidth(card_div)}`);

const tagsAndMaskList = document.querySelectorAll(".card_tags_and_mask_div");

// const divList = document.querySelectorAll(".card_tag_div");


for (const [index, element] of tagsAndMaskList.entries()) {
    console.log({index, element});
    
   //  console.log(`${element} overflow: ${checkOverflow(element)}`);
    console.log(`${element} width: ${element.offsetWidth}`);

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

   // console.log(`BEFORE CYCLE ${element} has oferflow == ${checkOverflow(element)}`);
   
   // console.log(`BEFORE CYCLE ${element} has width == ${getElementContentWidth(card_div)}`);

   


   while ( element.offsetWidth >  getElementContentWidth(card_div) ) {




      
      //   console.log(`${element} has overflow == ${checkOverflow(element)}`);
      console.log(`${element} has width == ${element.offsetWidth}`);
      
      let tagsDiv = element.querySelector(".card_tag_div") 
      console.log(`${tagsDiv} has children list with length of ${tagsDiv.children.length}`);


        let tagList = tagsDiv.children;
        let lastTag = tagList[tagList.length - 2]
        let text = lastTag.innerText;
        console.log(`${element} has last tag of: `, {text});

        console.log(`removing ${element}'s last tag `);
        tagsDiv.removeChild(lastTag);
        let resultingTagList = tagsDiv.children;
        console.log(`now ${tagsDiv}'s taglist is ... `, {resultingTagList});

        let tagWithTooltip = resultingTagList[resultingTagList.length - 1];
        console.log(`tagWithTooltip is ... `, {tagWithTooltip});
        

        let Tooltip = tagWithTooltip.children[tagWithTooltip.children.length - 1];
        console.log(`Tooltip div is ... `, {Tooltip});

        Tooltip.appendChild(lastTag);
        console.log(`Added ${text} tag to Tooltip `, {Tooltip});
        
    }


   //  console.log({element}, ` overflow is presumably: ${checkOverflow(element)} at last`)
    console.log({element}, ` width is presumably: ${element.offsetWidth} at last`)
}
