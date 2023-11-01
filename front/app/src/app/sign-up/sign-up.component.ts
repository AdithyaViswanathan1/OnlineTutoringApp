import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthenticationService } from '../authentication.service';
import { StudentSignupRequest } from '../models/StudentSignupRequest';
import { TutorSignupRequest } from '../models/TutorSignupRequest';
import { CookieService } from 'ngx-cookie-service';
import { RegisterRequest } from '../models/RegisterRequest';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.scss']
})
export class SignUpComponent implements OnInit {
  isStudent: boolean = true;
  missingFields: boolean = false;
  badPassword: boolean = false;
  noMatch: boolean = false;
  emailExists: boolean = false;


  fName: string = '';
  lName: string = '';
  email: string = '';
  password: string = '';
  cPassword: string = '';

  constructor(
    private route : ActivatedRoute,
    private router : Router,
    private authenticationService: AuthenticationService,
    private cookieService: CookieService) {
    this.route.params.subscribe(params => {
      this.isStudent = params['userType'] == 'student';
    });
  }

  ngOnInit(): void {
    if(this.authenticationService.isAuthenticated())
    {
      let userType = this.cookieService.get('userType');
      if(userType == 'student')
      {
        this.router.navigate(['/appointments']);
      }
      else if(userType == 'tutor')
      {
        this.router.navigate(['/profile', this.cookieService.get('userId')]);
      }
    }
  }

  signUp() {
    console.log('sign up');

    //check for missing fields
    if(this.fName == '' || this.lName == '' || this.email == '' || this.password == '' || this.cPassword == '') {
      this.missingFields = true;
      return;
    }
    else {
      this.missingFields = false;
    }

    //check for bad password
    const passwordRegex = /^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$/;
    if (!passwordRegex.test(this.password)) {
      this.badPassword = true;
      return;
    }
    else {
      this.badPassword = false;
    }

    // check if passwords match
    if (this.password !== this.cPassword) {
      this.noMatch = true;
      return;
    }
    else {
      this.noMatch = false;
    }

    //call auth service for user
    if(this.isStudent)
    {
      let request : RegisterRequest = {
        email: this.email,
        password: this.password,
        first_name: this.fName,
        last_name: this.lName,
        user_type: 'student'
      };

      this.authenticationService.studentSignup(request).subscribe(id => {
        this.cookieService.set('userId', id.toString());
        this.cookieService.set('userType', 'student');
        this.router.navigate(['/appointments']);
      });
    }
    else
    {
      let request : RegisterRequest = {
        email: this.email,
        password: this.password,
        first_name: this.fName,
        last_name: this.lName,
        user_type: 'tutor'
      };

      this.authenticationService.tutorSignUp(request).subscribe(id => {
        this.cookieService.set('userId', id.toString());
        this.cookieService.set('userType', 'tutor');
        this.router.navigate(['/profile', id]);
      });
    }
  }

  devCheatNav()
  {
    if(this.isStudent)
    {
      this.cookieService.set('userId', '1');
      this.cookieService.set('userType', 'student');
      this.router.navigate(['/appointments']);
    }
    else
    {
      this.cookieService.set('userId', '0');
      this.cookieService.set('userType', 'tutor');
      this.router.navigate(['/profile/0']);
    }
  }
}
