import { Component } from '@angular/core';
import {NavController, ToastController, Platform} from 'ionic-angular';
import { Camera} from 'ionic-native';
import { HTTP } from '@ionic-native/http';



declare var cordova: any;

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})

export class HomePage {
  public base64Image: string;
  private imageSrc: string;
  private storage: Storage;
  private http: HTTP;

  constructor(public navCtrl: NavController){
   }

public openGallery (): void {
  let cameraOptions = {
    sourceType: Camera.PictureSourceType.PHOTOLIBRARY,  //get the image from gallery
    destinationType: Camera.DestinationType.FILE_URI,   //return URI for image
    quality: 100,
    targetWidth: 1000,
    targetHeight: 1000,
    encodingType: Camera.EncodingType.JPEG,             //return the image in JPEG format
    correctOrientation: true
  }

  Camera.getPicture(cameraOptions)
        .then(file_uri => this.imageSrc = file_uri,
                             err => console.log(err));
          }

takePicture():void{
    Camera.getPicture({
        destinationType: Camera.DestinationType.NATIVE_URI,
        sourceType: Camera.PictureSourceType.CAMERA,
        targetWidth: 1000,
        targetHeight: 1000,
        saveToPhotoAlbum: true,
        encodingType: Camera.EncodingType.JPEG
    }).then(
        (imageData) => {
          this.base64Image = "data:image/jpeg;base64," + imageData;
    }, (err) => {
        console.log(err)
        });

    this.http.post("http://18.220.97.255", this.base64Image, {})
    }
    }



