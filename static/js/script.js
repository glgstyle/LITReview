function setStarsValue($event) {
    console.log("input target",$event.target)
    console.log("input target",$event.target.value)
    document.getElementById('result').setAttribute('value', $event.target.value)
    }
