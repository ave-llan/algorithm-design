var fs = require('fs');
var readline = require('readline');

var input = []
var filename = process.argv[2];
var compares = 0
readline.createInterface({
    input: fs.createReadStream(filename),
    terminal: false
}).on('line', function(line) {
  // console.log("line", line)
   input.push(Number(line))
}).on('close', function() {
  var array = input
  var sorted = quicksort(array, (a, b) => a < b)
  console.log(compares)
});;


function quicksort(a) {
  quicksortSub(a, 0, a.length - 1)
}

function quicksortSub(a, l, r) {

  if (r <= l) { return }
  compares += r - l
  // console.log('adding ' + (r - l))

  var j = partition(a, l, r)
  quicksortSub(a, l, j - 1)
  quicksortSub(a, j + 1, r)
}

function partition(a, l, r) {
  var p = choosePivot(a, l, r)
  swap(a, p, l)                       // move pivot to start
  var pivot = a[p]
  var i = l + 1

  for (var j = l + 1; j <= r; j++) {
    if (a[j] < pivot) {
      swap(a, j, i)
      i += 1
    }
  }

  swap(a, l, i - 1)                      // move pivot into place
  return i - 1
}

function choosePivot(a, l, r) {
  var mid = l + Math.floor((r - l) / 2)
  var three = [
    [a[l], l], 
    [a[mid], mid],
    [a[r], r]
  ]
  three.sort((a, b) => a[0] - b[0])
  return three[1][1]
  // return l
}

function swap(a, i, j) {
  var temp = a[i]
  a[i] = a[j]
  a[j] = temp 
}


// var test = [6,1,2,3,2,12, 1, -5, 3, 6]
// quicksort(test)
// console.log(test)
