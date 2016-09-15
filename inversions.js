var fs = require('fs');
var readline = require('readline');

var input = []
var filename = process.argv[2];
readline.createInterface({
    input: fs.createReadStream(filename),
    terminal: false
}).on('line', function(line) {
  // console.log("line", line)
   input.push(Number(line))
}).on('close', function() {
  console.log('goodbye!');
  console.log(input.length)
  var sorted = sortAndCountInversions(input, (a, b) => a < b)
  console.log(sorted.inversions)
});;


function sortAndCountInversions (array, isOrderedBefore) {
  if (array.length <= 1) {
    return { sorted: array, inversions: 0 }
  }

  var mid = Math.floor(array.length / 2)

  return mergeAndCountInversions(
    sortAndCountInversions(array.slice(0, mid), isOrderedBefore), 
    sortAndCountInversions(array.slice(mid)   , isOrderedBefore),
    isOrderedBefore
  )

}

function mergeAndCountInversions (left, right, isOrderedBefore) {
  var a = left.sorted, b = right.sorted
  var merged = [], i = 0, j = 0
  var splitInversions = 0
  while (i < a.length && j < b.length) {
    if (isOrderedBefore(a[i], b[j])) {
      merged.push(a[i])
      i += 1
    } else {
      merged.push(b[j])
      j += 1
      splitInversions += a.length - i
    }
  }
  // add any leftover
  merged = merged.concat(a.slice(i))
  merged = merged.concat(b.slice(j))
  return {
    sorted: merged,
    inversions: splitInversions + left.inversions + right.inversions
  }
}

// var test = [6,1,2,3,2,12, 1, -5, 3, 6]
// test = test.concat(test).concat(test).concat(test)

// var sorted = sortAndCountInversions(test, (a, b) => a < b)
// console.log(sorted)