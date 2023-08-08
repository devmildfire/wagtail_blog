// скрипт срабатывает на прогрузку страницы и на изменения размеров страницы
// он находит все переполняемые строки тэгов в карточках тэгов и перемещает 
// элементы, которые переполняют строку тэгов, в тултип

function getElementContentWidth(element) {
   var styles = window.getComputedStyle(element);
   var padding = parseFloat(styles.paddingLeft) +
   parseFloat(styles.paddingRight);
   
   return element.clientWidth - padding;
}

function fixOverFlow() {
   const card_div = document.querySelector(".card_div");
   // console.log(`Card Div `,{card_div}, ` width == ${getElementContentWidth(card_div)}`);
   
   const tagsAndMaskList = document.querySelectorAll(".card_tags_and_mask_div");
   
   for (const [index, element] of tagsAndMaskList.entries()) {
      // console.log({index, element});
       
      // console.log(`${element} width: ${element.offsetWidth}`);
   
   
      if ( element.offsetWidth >  getElementContentWidth(card_div) ) {    
   
         var tagWithTooltip = document.createElement("div");
         tagWithTooltip.classList.add("tag_with_tooltip_div")
   
         var tooltipDivAnchor = document.createElement("a");
         tooltipDivAnchor.classList.add("tag");
         tooltipDivAnchor.href = "#";
         tooltipDivAnchor.innerText = "+";
   
         tagWithTooltip.appendChild(tooltipDivAnchor);
   
         var tooltipDiv = document.createElement("div");
         tooltipDiv.classList.add("tooltip_div"); 
   
         tagWithTooltip.appendChild(tooltipDiv);
   
         var tagsDiv = element.querySelector(".card_tag_div"); 
         tagsDiv.appendChild(tagWithTooltip);
   
      }
   
   
      var iteration = 0;
   
      while ( element.offsetWidth >  getElementContentWidth(card_div) ) {
   
         // console.log(`${element} has width == ${element.offsetWidth}`);
         
         // console.log(`${tagsDiv} has children list with length of ${tagsDiv.children.length}`);
   
           iteration += 1;
   
           let tagList = tagsDiv.children;
           let lastTag = tagList[tagList.length - 2]
         //   let text = lastTag.innerText;
         //   console.log(`${element} has last tag of: `, {text});
   
         //   console.log(`removing ${element}'s last tag `);
           tagsDiv.removeChild(lastTag);
         //   let resultingTagList = tagsDiv.children;
         //   console.log(`now ${tagsDiv}'s taglist is ... `, {resultingTagList});
   
         //   console.log(`tagWithTooltip is ... `, {tagWithTooltip});
           
         //   console.log(`Tooltip div is ... `, {tooltipDiv});
   
           tooltipDiv.appendChild(lastTag);
         //   console.log(`Added ${text} tag to Tooltip `, {tooltipDiv});
   
           tooltipDivAnchor.innerText = `+ ${iteration}`;
           
       }
   
      console.log({element}, ` width is presumably: ${element.offsetWidth} at last`)
   }
   
}


fixOverFlow();