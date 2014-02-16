var coffee = require('coffee-script'),
    source = '';

process.stdin.resume();
process.stdin.setEncoding('utf8');

process.stdin.on('data', function(chunk) {
  source += chunk;
});

process.stdin.on('end', function() {
  var bare = process.argv[2] == '--bare';
  process.stdout.write(coffee.compile(source, {bare: bare}));
});
