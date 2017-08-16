import { Component } from '@angular/core';
import { NavController, NavParams } from 'ionic-angular';
import { HTTP } from '@ionic-native/http';


@Component({
  selector: 'page-editfile',
  templateUrl: 'editfile.html',
})
export class EditfilePage {

  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad EditfilePage');
  }
  words = ["Hello", "Goodbye"];
  body: {
    words = [];
  };
  body.words = words;
  this.http.post('http://ec2-18-220-97-255.us-east-2.compute.amazonaws.com/uploads', body, {})
  .then(data => {
      console.log(data.status);
				console.log(data.data); // data received by server
				console.log(data.headers);

        //var received = data.data;

				let alert = this.alertCtrl.create({
					title: 'Success',
					subTitle: data.data,
					buttons: ['Dismiss']
				});
				alert.present();
			})
			.catch(error => {

				console.log(error.status);
				console.log(error.error); // error message as string
				console.log(error.headers);

				let alert = this.alertCtrl.create({
					title: error.headers[1],
					subTitle: error.error,
					buttons: ['Ok']
				});
				alert.present();
			});

		}, (err) => {
			// Handle error
		});

}
