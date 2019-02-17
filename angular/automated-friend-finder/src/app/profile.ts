import { Event } from './event';
export class Profile {
    name: string;
    age: number;
    gender: string;
    country: string;
    acceptable_country: string[];
    acceptable_age_range: {
        start: number;
        end: number;
    }
    likes: string[];
    dislikes: string[];
    books: string[];
    eventCategory: string;
    listOfEvents: Event[];
}