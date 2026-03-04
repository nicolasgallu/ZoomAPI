//Nicolas testea la Api de Zoom :)

//interfaces demo
interface PlanetWeather {
	PlanetName:string,
	Temperature:number,
	HasAtmosphere:boolean,
	Moons:number
}

const tatooine : PlanetWeather = {
	PlanetName:"tatooine",
	Temperature:20,
	HasAtmosphere:false,
	Moons:213
}
console.log(tatooine)

//arrays

interface Episode {
	title: string,
	year: number
}

interface StarWarsMovie {
	id:number,
	director: string,
	episodes: Episode[]
}

const OriginalTrilogy: StarWarsMovie = {
	id: 1,
	director: "George Lucas",
	episodes: [{title:"one",year:1999}, {title:"two",year:2005}]
	

}

console.log(OriginalTrilogy)


