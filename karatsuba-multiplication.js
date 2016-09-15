
function multiply (x, y) {
  if (len(x) == 1) {
    return x * y
  }

}


function len (number) {
  return String(number).length
}

function splitNum(number) {
  var stringNum = String(number),
        halfway = Math.floor(stringNum.length / 2)

  return [
    stringNum.slice(0, halfway),
    stringNum.slice(halfway)
  ].map(str => Number(str))
}

