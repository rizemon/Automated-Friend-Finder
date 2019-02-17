import { Component, OnInit } from '@angular/core';
import { ProfileService } from '../profile.service';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(public profileService:ProfileService) { }

  ngOnInit() {
    this.profileService.getAll();
    this.profileService.setTitle("Log in as...");
  }

}
