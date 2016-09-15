
function bottomUpMergeSort (array, isOrderedBefore) {
  var aux = new Array(array.length)

  function merge (array, leftStart, rightStart, end) {
    
    for (var i = leftStart; i < end; i++) {
      aux[i] = array[i]
    }

    var l = leftStart, r = rightStart
    for (var i = leftStart; i < end; i++) {
      if      (l >= rightStart) 
        array[i] = aux[r++]
      else if (r >= end)        
        array[i] = aux[l++]
      else if (isOrderedBefore(aux[l], aux[r]))
        array[i] = aux[l++]
      else 
        array[i] = aux[r++]
    }
  }

  var orderedLength = 1
  while (orderedLength < array.length) {
    console.log(`ordered length: ${orderedLength}`)
    console.log(array)
    for (i = 0; i + orderedLength < array.length; i += orderedLength * 2) {
      merge(array, i, i + orderedLength, Math.min(i + orderedLength * 2, array.length))
    }
    orderedLength *= 2
  }

  return array
}

var test = [6,1,2,3,2,12, 1, -5, 3, 6, -10, 1, 2, 2, 2, 2, 23, 1, 5, 3, -17, 4, 0, 1 ,2, 4, 3]

var sorted = bottomUpMergeSort(test, (a, b) => a < b)
console.log(sorted)

