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
   // const card_div = document.querySelector(".card_div");
   const card_div = document.querySelector(".card_image");

   // console.log(`Card Div `,{card_div}, ` width == ${getElementContentWidth(card_div)}`);
   
   const tagsAndMaskList = document.querySelectorAll(".card_tags_and_mask_div");
   
   for (const [index, element]  of tagsAndMaskList.entries()) {
      // console.log({index, element});
       
      // console.log(`${element} width: ${element.offsetWidth}`);
   
   
      if ( element.offsetWidth >  card_div.offsetWidth+1 ) {    
      // if ( element.offsetWidth >  327 ) {    
   
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

      console.log({element});

      // var tagListInitialCount = tagsDiv.childElementCount;

      var tagsDiv = element.querySelector(".card_tag_div"); 

      // console.log({tagsDiv});

      var forLength = tagsDiv.children;
      var count = forLength.length
      var tagListInitialCount = count;

      console.log(` tagListInitialCount = `, tagListInitialCount);

   
      while ((iteration < tagListInitialCount) && ( element.offsetWidth >  card_div.offsetWidth+1 )) {
      // while ((iteration < tagListInitialCount) && ( element.offsetWidth >  327 )) {
   
      console.log(` card_div_width + 1 = `, card_div.offsetWidth + 1);

      console.log(` element  Width = `, element.offsetWidth);
      
   
           iteration += 1;
   
           let tagList = tagsDiv.children;
           console.log(`tagList is: `, {tagList});

            if(tagList.length > 2) {

               let lastTag = tagList[tagList.length - 2];
               console.log(`last tag is: `, {lastTag});
               tagsDiv.removeChild(lastTag);

               tooltipDiv.appendChild(lastTag);
               tooltipDivAnchor.innerText = `+ ${iteration}`;
            }
           
       }
   
      console.log({element}, ` width is presumably: ${element.offsetWidth} at last`)

      console.log(` card_div_width + 1 = `, card_div.offsetWidth + 1);

      
   }
   
}


document.addEventListener("DOMContentLoaded", function(){
   fixOverFlow();
   console.log('Oferflows all fixed ad DOM load');
});


window.onresize = function() {
   fixOverFlow();
   console.log('Oferflows all fixed ad WINDOW RESIZE load');
};