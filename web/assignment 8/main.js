const customName = document.getElementById('customname');
const randomize = document.querySelector('.randomize');
const story = document.querySelector('.story');

function randomValueFromArray(array){
  const random = Math.floor(Math.random()*array.length);
  return array[random];
}

let storyText = 'It was 94 fahrenheit outside, so :insertx: went for a walk. When they got to :inserty:, their mouths dropped open in shock, then :insertz:. Bob saw the whole thing, but was not surprised — :insertx: weighs 300 pounds, and it was a hot day.'

let insertX = ['Belly the bulldog',
'Easter Bunny',
'frank the cricket']

let insertY = ['the bathtub',
'magic mountain',
'Florida']

let insertZ = ['flew away with the birds',
'fell into a sinkhole',
'discovered a hidden treasure']

randomize.addEventListener('click', result);

function result() { 

    let newStory = storyText

    let xItem = randomValueFromArray(insertX);
    let yItem = randomValueFromArray(insertY);
    let zItem = randomValueFromArray(insertZ);
    console.log(xItem)
    newStory = newStory.replace(':insertx:', xItem);
    newStory = newStory.replace(':insertx:', xItem);
    newStory = newStory.replace(':inserty:', yItem);
    newStory = newStory.replace(':insertz:', zItem);

    if(customName.value !== '') {
        const name = customName.value;
        newStory = newStory.replace('Bob', name);

    }

    if(document.getElementById("uk").checked) {
        const weight = Math.round(300 * 0.07142792343282228229);
        const temperature =  Math.round((94- 32) * 5/9);
        newStory = newStory.replace('94 fahrenheit', temperature+' celcius');
        newStory = newStory.replace('300 pounds', weight+' stone');
  
    }

    story.textContent = newStory;
    story.style.visibility = 'visible';
}

