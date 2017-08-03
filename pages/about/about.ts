import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import {Flashcard1Page} from '../flashcard1/flashcard1';


@Component({
  selector: 'page-about',
  templateUrl: 'about.html'
})

export class AboutPage {

  constructor(public navCtrl: NavController) {
    this.navCtrl = navCtrl;
  }

  public navPush() {
    this.navCtrl.push(Flashcard1Page);
  }
}
