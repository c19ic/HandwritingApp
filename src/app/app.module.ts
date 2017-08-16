import { NgModule, ErrorHandler } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { IonicApp, IonicModule, IonicErrorHandler } from 'ionic-angular';
import { MyApp } from './app.component';
import {Camera, CameraOptions} from '@ionic-native/camera';
import { AboutPage } from '../pages/about/about';
import { Flashcard1Page } from '../pages/flashcard1/flashcard1';
import { HomePage } from '../pages/home/home';
import { TabsPage } from '../pages/tabs/tabs';
import { FlashCardComponent } from '../components/flash-card/flash-card';
import { EditfilePage } from '../pages/editfile/editfile' ;
import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';
import { NavController, AlertController } from 'ionic-angular';
import { HTTP } from '@ionic-native/http' ;
import { IonicStorageModule } from '@ionic/storage';
import { Transfer, FileUploadOptions, TransferObject } from '@ionic-native/transfer';
import {File} from '@ionic-native/file';
import { FileTransfer, FileTransferObject } from '@ionic-native/file-transfer';

@NgModule({
  declarations: [
    MyApp,
    AboutPage,
    HomePage,
    TabsPage,
    Flashcard1Page,
    FlashCardComponent,
    EditfilePage,
  ],
  imports: [
    BrowserModule,
    IonicModule.forRoot(MyApp),
    IonicStorageModule.forRoot(),
    ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    AboutPage,
    HomePage,
    TabsPage,
    Flashcard1Page,
    EditfilePage,
  ],
  providers: [
    StatusBar,
    SplashScreen,
    Camera,
    Transfer,
    File,
    HTTP,
    FileTransfer,
    {provide: ErrorHandler, useClass: IonicErrorHandler}
  ]
})
export class AppModule {}
