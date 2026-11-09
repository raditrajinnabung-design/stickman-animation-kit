// Toon animation kit
export interface ToonCharacter {
  name: string;
  color: string;
  x: number;
  y: number;
}

export function createToonCharacter(
  name: string,
  color = "#000000",
  x = 0,
  y = 0
): ToonCharacter {
  return {
    name,
    color,
    x,
    y
  };
}

export function moveToon(
  character: ToonCharacter,
  x: number,
  y: number
): ToonCharacter {
  return {
    ...character,
    x,
    y
  };
}
