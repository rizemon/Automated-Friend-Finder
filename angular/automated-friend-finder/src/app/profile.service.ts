import { Injectable } from '@angular/core';
import { Profile } from './profile';
import { Response } from './response';
import { HttpClient } from '@angular/common/http';
import { MatSnackBar } from '@angular/material';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ProfileService {
  profiles: Profile[] = [];
  title: string = "";
  current_profile: string = "";
  chart: string = "";
  profile: Profile = null;

  constructor(private httpClient: HttpClient,private snackBar: MatSnackBar) { 
  };

  getSingle(name: string){
    this.setTitle(`Currently viewing ${name}'s profile`);
    this.setProfiles([]);
    this.setChart("");
    this.httpClient.get<Profile>(environment.API_URL + "/single",{params:{"profile_name":name}})
      .subscribe((res)=>this.setProfile(res));
    console.log(this.profiles.length == 0);
    
  }

  getAll(){
    this.setTitle("All profiles");
    this.httpClient.get<Profile[]>(environment.API_URL + "/all",{params:{"current_profile":this.current_profile}})
      .subscribe((res)=> this.setProfiles(res));
    this.setChart("");
    this.setProfile(null);
  }

  getCountry(){
    this.setTitle("Filtered by acceptable country");
    this.httpClient.get<Profile[]>(environment.API_URL + "/bestmatch/country",{params:{"current_profile":this.current_profile}})
      .subscribe((res)=> this.setProfiles(res));
    this.setChart("");
    this.setProfile(null);
  }

  getLikes(){
    this.setTitle("Top 3 best matches based on likes");
    this.httpClient.get<Profile[]>(environment.API_URL + "/bestmatch/likes",{params:{"current_profile":this.current_profile}})
      .subscribe((res)=> this.setProfiles(res));
    this.setChart("");
    this.setProfile(null);
  }

  getDislikes(){
    this.setTitle("Top 3 best matches based on dislikes");
    this.httpClient.get<Profile[]>(environment.API_URL + "/bestmatch/dislikes",{params:{"current_profile":this.current_profile}})
      .subscribe((res)=> this.setProfiles(res));
    this.setChart("");
    this.setProfile(null);
  }

  getBookInterests(){
    this.setTitle("Top 3 best matches based on interests");
    this.httpClient.get<Profile[]>(environment.API_URL + "/bestmatch/books",{params:{"current_profile":this.current_profile}})
      .subscribe((res)=> this.setProfiles(res));
    this.setChart("");
    this.setProfile(null);
  }

  getOverallInfo(){
    this.setTitle("Top 3 best matches based on overall information");
    this.httpClient.get<Profile[]>(environment.API_URL + "/bestmatch/overall",{params:{"current_profile":this.current_profile}})
      .subscribe((res)=> this.setProfiles(res));
    this.setChart("");
    this.setProfile(null);
  }

  getDateSuggestions(){
    this.setTitle("Date suggestions for top 3 best matches based on overall information");
    this.httpClient.get<Profile[]>(environment.API_URL + "/bestmatch/suggestion",{params:{"current_profile":this.current_profile}})
      .subscribe((res)=> this.setProfiles(res));
    this.setChart("");
    this.setProfile(null);
  }

  getLikesChart(){
    this.setTitle("Top likes by percentage");
    this.setProfiles([]);
    this.setChart(environment.API_URL + "/piechart/likes");
    this.setProfile(null);
  }

  getDislikesChart(){
    this.setTitle("Top dislikes by percentage");
    this.setProfiles([]);
    this.setChart(environment.API_URL + "/piechart/dislikes");
    this.setProfile(null);
  }

  getCountryChart(){
    this.setTitle("Top nationalities by percentage");
    this.setProfiles([]);
    this.setChart(environment.API_URL + "/piechart/country");
    this.setProfile(null);
  }

  getAgeChart(){
    this.setTitle("Top ages by percentage");
    this.setProfiles([]);
    this.setChart(environment.API_URL + "/piechart/age");
    this.setProfile(null);
  }

  getCSV(){
    this.httpClient.post<Response>(environment.API_URL + "/csv",{"current_profile":this.current_profile})
      .subscribe((res)=> this.showMessage("Saved in: " + res.message));
  }

  setTitle(title:string){
    this.title = title;
  }

  setCurrentProfile(name: string){
    this.current_profile = name;
  }

  setProfile(profile: Profile){
    this.profile = profile;
  }

  setProfiles(profiles: Profile[]){
    this.profiles = profiles
  }

  setChart(type: string){
    this.chart = type;
  }

  showMessage(message: string){
    this.snackBar.open(message,"Close",{
      duration: 2000,
    });
  }

}
