const cars = [
  {"name": "Aston Martin", "price": 50000, "year": 2012},
  {"name": "BMW", "price": 30000, "year": 2014},
  {"name": "Chevrolet", "price": 20000, "year": 2013},
  {"name": "Datsun", "price": 2000, "year": 2001},
];

function findOldestCar(cars) {
  let min_year = -1;
  let oldest_car = cars[0];
  for (let i = 0; i < cars.length; i++) {
    let car = cars[i];
    if (car["year"] < min_year || min_year === -1) {
      min_year = car["year"];
      oldest_car = car;
    }
  }
  return oldest_car;
}

function findHighestPrice(cars) {
  let max_price = -1;
  let expensive_car = cars[0];
  for (let i = 0; i < cars.length; i++) {
    let car = cars[i];
    if (car["price"] > max_price || max_price === -1) {
      max_price = car["price"];
      expensive_car = car;
    }
  }
  return expensive_car;
}

console.log(cars);

console.log(findOldestCar(cars));
console.log(findHighestPrice(cars));