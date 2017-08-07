import { Component, ElementRef, ViewChild } from '@angular/core';
import { NavController } from 'ionic-angular';
import {Flashcard1Page} from '../flashcard1/flashcard1';

@Component({
  selector: 'page-about',
  templateUrl: 'about.html'
})
export class AboutPage {
  @ViewChild('fcContainer') fcContainer;
  @ViewChild('front') fcFront;
  @ViewChild('back') fcBack;
   toggled: boolean = false;
 
  constructor(public navCtrl: NavController) {
    this.navCtrl = navCtrl;
  }
  public navPush() {
    this.navCtrl.push(Flashcard1Page);
  }
  ngAfterViewChecked(){
    let frontH = this.fcFront.nativeElement.querySelector('.fc-front').offsetHeight + 40;
    let backH = this.fcBack.nativeElement.querySelector('.fc-back').offsetHeight + 40;
    let h = ((frontH > backH)? frontH:backH) + 'px';
    this.fcContainer.nativeElement.style.height = h;
    this.fcBack.nativeElement.style.height = h;
    this.fcFront.nativeElement.style.height = h;
  }
  toggle() {
    this.toggled = !this.toggled;
  }

}
