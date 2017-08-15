import { Component } from '@angular/core';
import {NavController, ToastController, Platform, AlertController } from 'ionic-angular';
import {Camera, CameraOptions} from '@ionic-native/camera';
import { HTTP } from '@ionic-native/http';
import { File } from '@ionic-native/file';
import { FileTransfer, FileTransferObject } from '@ionic-native/file-transfer';


declare var cordova: any;

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})

export class HomePage {
  public base64Image: string;
  private imageSrc: string;

  constructor(public navCtrl: NavController, private camera: Camera, private http: HTTP, private alertCtrl: AlertController){}

public openGallery (): void {
  let cameraOptions = {
    sourceType: this.camera.PictureSourceType.PHOTOLIBRARY,  //get the image from gallery
    destinationType: 1,   //return URI for image
    quality: 100,
    targetWidth: 1000,
    targetHeight: 1000,
    encodingType: this.camera.EncodingType.JPEG,             //return the image in JPEG format
    correctOrientation: true
  }

  this.camera.getPicture(cameraOptions)
        .then(file_uri => this.imageSrc = file_uri,
                             err => console.log(err));
          }

takePicture(): void{
    const options: CameraOptions = {
        destinationType: 1,
        sourceType: this.camera.PictureSourceType.CAMERA,
        targetWidth: 1000,
        targetHeight: 1000,
        saveToPhotoAlbum: true,
        encodingType: this.camera.EncodingType.JPEG,
        mediaType: this.camera.MediaType.PICTURE
    }

		this.camera.getPicture(options).then((imagePath) => {
			 // imageData is either a base64 encoded string or a file URI
			 // If it's base64:
			// let base64Image = 'data:image/jpeg;base64,' + imageData;

			let alert = this.alertCtrl.create({
				title: 'Picture taken:',
				subTitle: imagePath,
				buttons: ['Dismiss']
			});
			alert.present();

			this.http.uploadFile('http://ec2-18-220-97-255.us-east-2.compute.amazonaws.com/uploads', {}, {}, imagePath, "file")
			.then(data => {

				console.log(data.status);
				console.log(data.data); // data received by server
				console.log(data.headers);

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
}
