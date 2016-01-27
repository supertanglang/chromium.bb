# Copyright 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'blink_public_sources': [
      "platform/Platform.h",
      "platform/WebApplicationCacheHost.h",
      "platform/WebApplicationCacheHostClient.h",
      "platform/WebAudioBus.h",
      "platform/WebAudioDestinationConsumer.h",
      "platform/WebAudioDevice.h",
      "platform/WebAudioSourceProvider.h",
      "platform/WebAudioSourceProviderClient.h",
      "platform/WebBatteryStatus.h",
      "platform/WebBatteryStatusListener.h",
      "platform/WebBlendMode.h",
      "platform/WebBlobData.h",
      "platform/WebBlobInfo.h",
      "platform/WebBlobRegistry.h",
      "platform/WebCString.h",
      "platform/WebCallbacks.h",
      "platform/WebCanvas.h",
      "platform/WebCircularGeofencingRegion.h",
      "platform/WebClipboard.h",
      "platform/WebColor.h",
      "platform/WebCommon.h",
      "platform/WebCompositeAndReadbackAsyncCallback.h",
      "platform/WebCompositedDisplayList.h",
      "platform/WebCompositorAnimation.h",
      "platform/WebCompositorAnimationCurve.h",
      "platform/WebCompositorAnimationDelegate.h",
      "platform/WebCompositorAnimationPlayer.h",
      "platform/WebCompositorAnimationPlayerClient.h",
      "platform/WebCompositorAnimationTimeline.h",
      "platform/WebCompositorSupport.h",
      "platform/WebConnectionType.h",
      "platform/WebContentDecryptionModule.h",
      "platform/WebContentDecryptionModuleAccess.h",
      "platform/WebContentDecryptionModuleException.h",
      "platform/WebContentDecryptionModuleResult.h",
      "platform/WebContentDecryptionModuleSession.h",
      "platform/WebContentLayer.h",
      "platform/WebContentLayerClient.h",
      "platform/WebContentSettingCallbacks.h",
      "platform/WebConvertableToTraceFormat.h",
      "platform/WebCookieJar.h",
      "platform/WebCredential.h",
      "platform/WebCredentialManagerClient.h",
      "platform/WebCredentialManagerError.h",
      "platform/WebCrossOriginServiceWorkerClient.h",
      "platform/WebCrypto.h",
      "platform/WebCryptoAlgorithm.h",
      "platform/WebCryptoAlgorithmParams.h",
      "platform/WebCryptoKey.h",
      "platform/WebCryptoKeyAlgorithm.h",
      "platform/WebCryptoKeyAlgorithmParams.h",
      "platform/WebCursorInfo.h",
      "platform/WebData.h",
      "platform/WebDataConsumerHandle.h",
      "platform/WebDatabaseObserver.h",
      "platform/WebDeviceLightListener.h",
      "platform/WebDiscardableMemory.h",
      "platform/WebDisplayItemClipTree.h",
      "platform/WebDisplayItemList.h",
      "platform/WebDisplayItemTransformTree.h",
      "platform/WebDisplayMode.h",
      "platform/WebDoublePoint.h",
      "platform/WebDragData.h",
      "platform/WebEncryptedMediaClient.h",
      "platform/WebEncryptedMediaKeyInformation.h",
      "platform/WebEncryptedMediaRequest.h",
      "platform/WebEncryptedMediaTypes.h",
      "platform/WebExternalBitmap.h",
      "platform/WebExternalTextureLayer.h",
      "platform/WebExternalTextureLayerClient.h",
      "platform/WebExternalTextureMailbox.h",
      "platform/WebFallbackThemeEngine.h",
      "platform/WebFederatedCredential.h",
      "platform/WebFileError.h",
      "platform/WebFileInfo.h",
      "platform/WebFileSystem.h",
      "platform/WebFileSystemCallbacks.h",
      "platform/WebFileSystemEntry.h",
      "platform/WebFileSystemType.h",
      "platform/WebFileUtilities.h",
      "platform/WebFileWriter.h",
      "platform/WebFileWriterClient.h",
      "platform/WebFilterAnimationCurve.h",
      "platform/WebFilterKeyframe.h",
      "platform/WebFilterOperations.h",
      "platform/WebFlingAnimator.h",
      "platform/WebFloatAnimationCurve.h",
      "platform/WebFloatKeyframe.h",
      "platform/WebFloatPoint.h",
      "platform/WebFloatPoint3D.h",
      "platform/WebFloatRect.h",
      "platform/WebFloatSize.h",
      "platform/WebFocusType.h",
      "platform/WebFrameHostScheduler.h",
      "platform/WebFrameScheduler.h",
      "platform/WebFrameTimingEvent.h",
      "platform/WebGamepad.h",
      "platform/WebGamepadListener.h",
      "platform/WebGamepads.h",
      "platform/WebGeofencingError.h",
      "platform/WebGeofencingEventType.h",
      "platform/WebGeofencingProvider.h",
      "platform/WebGeofencingRegistration.h",
      "platform/WebGestureCurve.h",
      "platform/WebGestureCurveTarget.h",
      "platform/WebGestureDevice.h",
      "platform/WebGraphicsContext3D.h",
      "platform/WebGraphicsContext3DProvider.h",
      "platform/WebGraphicsLayerDebugInfo.h",
      "platform/WebHTTPBody.h",
      "platform/WebHTTPHeaderVisitor.h",
      "platform/WebHTTPLoadInfo.h",
      "platform/WebHistoryScrollRestorationType.h",
      "platform/WebImage.h",
      "platform/WebImageGenerator.h",
      "platform/WebImageLayer.h",
      "platform/WebInbandTextTrack.h",
      "platform/WebInbandTextTrackClient.h",
      "platform/WebLayer.h",
      "platform/WebLayerClient.h",
      "platform/WebLayerPositionConstraint.h",
      "platform/WebLayerScrollClient.h",
      "platform/WebLayerTreeView.h",
      "platform/WebLayoutAndPaintAsyncCallback.h",
      "platform/WebLocalizedString.h",
      "platform/WebMIDIAccessor.h",
      "platform/WebMIDIAccessorClient.h",
      "platform/WebMediaConstraints.h",
      "platform/WebMediaDeviceInfo.h",
      "platform/WebMediaKeySystemConfiguration.h",
      "platform/WebMediaKeySystemMediaCapability.h",
      "platform/WebMediaPlayer.h",
      "platform/WebMediaPlayerClient.h",
      "platform/WebMediaRecorderHandler.h",
      "platform/WebMediaRecorderHandlerClient.h",
      "platform/WebMediaSource.h",
      "platform/WebMediaStream.h",
      "platform/WebMediaStreamCenter.h",
      "platform/WebMediaStreamCenterClient.h",
      "platform/WebMediaStreamSource.h",
      "platform/WebMediaStreamTrack.h",
      "platform/WebMediaStreamTrackSourcesRequest.h",
      "platform/WebMemoryAllocatorDump.h",
      "platform/WebMemoryDumpProvider.h",
      "platform/WebMessagePortChannel.h",
      "platform/WebMessagePortChannelClient.h",
      "platform/WebMimeRegistry.h",
      "platform/WebNonCopyable.h",
      "platform/WebPageVisibilityState.h",
      "platform/WebPasswordCredential.h",
      "platform/WebPlatformEventListener.h",
      "platform/WebPlatformEventType.h",
      "platform/WebPluginListBuilder.h",
      "platform/WebPoint.h",
      "platform/WebPrerender.h",
      "platform/WebPrerenderingSupport.h",
      "platform/WebPrescientNetworking.h",
      "platform/WebPrivateOwnPtr.h",
      "platform/WebPrivatePtr.h",
      "platform/WebProcessMemoryDump.h",
      "platform/WebPublicSuffixList.h",
      "platform/WebRTCConfiguration.h",
      "platform/WebRTCDTMFSenderHandler.h",
      "platform/WebRTCDTMFSenderHandlerClient.h",
      "platform/WebRTCDataChannelHandler.h",
      "platform/WebRTCDataChannelHandlerClient.h",
      "platform/WebRTCDataChannelInit.h",
      "platform/WebRTCICECandidate.h",
      "platform/WebRTCOfferOptions.h",
      "platform/WebRTCPeerConnectionHandler.h",
      "platform/WebRTCPeerConnectionHandlerClient.h",
      "platform/WebRTCSessionDescription.h",
      "platform/WebRTCSessionDescriptionRequest.h",
      "platform/WebRTCStatsRequest.h",
      "platform/WebRTCStatsResponse.h",
      "platform/WebRTCVoidRequest.h",
      "platform/WebRect.h",
      "platform/WebReferrerPolicy.h",
      "platform/WebRenderingStats.h",
      "platform/WebScheduler.h",
      "platform/WebScreenInfo.h",
      "platform/WebScrollBlocksOn.h",
      "platform/WebScrollOffsetAnimationCurve.h",
      "platform/WebScrollbar.h",
      "platform/WebScrollbarBehavior.h",
      "platform/WebScrollbarLayer.h",
      "platform/WebScrollbarThemeGeometry.h",
      "platform/WebScrollbarThemePainter.h",
      "platform/WebSecurityOrigin.h",
      "platform/WebSelectionBound.h",
      "platform/WebServiceWorker.h",
      "platform/WebServiceWorkerCache.h",
      "platform/WebServiceWorkerCacheError.h",
      "platform/WebServiceWorkerCacheStorage.h",
      "platform/WebServiceWorkerClientQueryOptions.h",
      "platform/WebServiceWorkerClientType.h",
      "platform/WebServiceWorkerClientsClaimCallbacks.h",
      "platform/WebServiceWorkerClientsInfo.h",
      "platform/WebServiceWorkerError.h",
      "platform/WebServiceWorkerEventResult.h",
      "platform/WebServiceWorkerProvider.h",
      "platform/WebServiceWorkerProviderClient.h",
      "platform/WebServiceWorkerProxy.h",
      "platform/WebServiceWorkerRegistration.h",
      "platform/WebServiceWorkerRegistrationProxy.h",
      "platform/WebServiceWorkerRequest.h",
      "platform/WebServiceWorkerResponse.h",
      "platform/WebServiceWorkerResponseType.h",
      "platform/WebServiceWorkerSkipWaitingCallbacks.h",
      "platform/WebServiceWorkerState.h",
      "platform/WebSetSinkIdError.h",
      "platform/WebSize.h",
      "platform/WebSocketHandle.h",
      "platform/WebSocketHandleClient.h",
      "platform/WebSocketHandshakeRequestInfo.h",
      "platform/WebSocketHandshakeResponseInfo.h",
      "platform/WebSourceBuffer.h",
      "platform/WebSourceBufferClient.h",
      "platform/WebSourceInfo.h",
      "platform/WebSpeechSynthesisUtterance.h",
      "platform/WebSpeechSynthesisVoice.h",
      "platform/WebSpeechSynthesizer.h",
      "platform/WebSpeechSynthesizerClient.h",
      "platform/WebStorageArea.h",
      "platform/WebStorageNamespace.h",
      "platform/WebStorageQuotaCallbacks.h",
      "platform/WebStorageQuotaError.h",
      "platform/WebStorageQuotaType.h",
      "platform/WebString.h",
      "platform/WebSuspendableTask.h",
      "platform/WebTaskRunner.h",
      "platform/WebThemeEngine.h",
      "platform/WebThread.h",
      "platform/WebThreadSafeData.h",
      "platform/WebThreadedDataReceiver.h",
      "platform/WebTimeRange.h",
      "platform/WebTopControlsState.h",
      "platform/WebTraceLocation.h",
      "platform/WebTransformAnimationCurve.h",
      "platform/WebTransformKeyframe.h",
      "platform/WebTransformOperations.h",
      "platform/WebURL.h",
      "platform/WebURLError.h",
      "platform/WebURLLoadTiming.h",
      "platform/WebURLLoader.h",
      "platform/WebURLLoaderClient.h",
      "platform/WebURLRequest.h",
      "platform/WebURLResponse.h",
      "platform/WebUnitTestSupport.h",
      "platform/WebVector.h",
      "platform/WebWaitableEvent.h",
      "platform/linux/WebFallbackFont.h",
      "platform/linux/WebFontInfo.h",
      "platform/linux/WebFontRenderStyle.h",
      "platform/linux/WebSandboxSupport.h",
      "platform/mac/WebSandboxSupport.h",
      "platform/modules/app_banner/WebAppBannerClient.h",
      "platform/modules/app_banner/WebAppBannerPromptReply.h",
      "platform/modules/app_banner/WebAppBannerPromptResult.h",
      "platform/modules/background_sync/WebSyncClient.h",
      "platform/modules/background_sync/WebSyncError.h",
      "platform/modules/background_sync/WebSyncPermissionStatus.h",
      "platform/modules/background_sync/WebSyncProvider.h",
      "platform/modules/background_sync/WebSyncRegistration.h",
      "platform/modules/bluetooth/WebBluetooth.h",
      "platform/modules/bluetooth/WebBluetoothDevice.h",
      "platform/modules/bluetooth/WebBluetoothError.h",
      "platform/modules/bluetooth/WebBluetoothGATTCharacteristicInit.h",
      "platform/modules/bluetooth/WebBluetoothGATTRemoteServer.h",
      "platform/modules/bluetooth/WebBluetoothGATTService.h",
      "platform/modules/bluetooth/WebRequestDeviceOptions.h",
      "platform/modules/device_orientation/WebDeviceMotionData.h",
      "platform/modules/device_orientation/WebDeviceMotionListener.h",
      "platform/modules/device_orientation/WebDeviceOrientationData.h",
      "platform/modules/device_orientation/WebDeviceOrientationListener.h",
      "platform/modules/indexeddb/WebIDBCallbacks.h",
      "platform/modules/indexeddb/WebIDBCursor.h",
      "platform/modules/indexeddb/WebIDBDatabase.h",
      "platform/modules/indexeddb/WebIDBDatabaseCallbacks.h",
      "platform/modules/indexeddb/WebIDBDatabaseError.h",
      "platform/modules/indexeddb/WebIDBDatabaseException.h",
      "platform/modules/indexeddb/WebIDBFactory.h",
      "platform/modules/indexeddb/WebIDBKey.h",
      "platform/modules/indexeddb/WebIDBKeyPath.h",
      "platform/modules/indexeddb/WebIDBKeyRange.h",
      "platform/modules/indexeddb/WebIDBMetadata.h",
      "platform/modules/indexeddb/WebIDBTypes.h",
      "platform/modules/indexeddb/WebIDBValue.h",
      "platform/modules/navigator_services/WebServicePort.h",
      "platform/modules/navigator_services/WebServicePortProvider.h",
      "platform/modules/navigator_services/WebServicePortProviderClient.h",
      "platform/modules/notifications/WebNotificationAction.h",
      "platform/modules/notifications/WebNotificationData.h",
      "platform/modules/notifications/WebNotificationDelegate.h",
      "platform/modules/notifications/WebNotificationManager.h",
      "platform/modules/notifications/WebNotificationPermission.h",
      "platform/modules/permissions/WebPermissionClient.h",
      "platform/modules/permissions/WebPermissionObserver.h",
      "platform/modules/permissions/WebPermissionStatus.h",
      "platform/modules/permissions/WebPermissionType.h",
      "platform/modules/presentation/WebPresentationClient.h",
      "platform/modules/presentation/WebPresentationController.h",
      "platform/modules/presentation/WebPresentationError.h",
      "platform/modules/presentation/WebPresentationSessionClient.h",
      "platform/modules/push_messaging/WebPushClient.h",
      "platform/modules/push_messaging/WebPushError.h",
      "platform/modules/push_messaging/WebPushPermissionStatus.h",
      "platform/modules/push_messaging/WebPushProvider.h",
      "platform/modules/push_messaging/WebPushSubscription.h",
      "platform/modules/push_messaging/WebPushSubscriptionOptions.h",
      "platform/modules/screen_orientation/WebLockOrientationCallback.h",
      "platform/modules/screen_orientation/WebLockOrientationError.h",
      "platform/modules/screen_orientation/WebScreenOrientationClient.h",
      "platform/modules/screen_orientation/WebScreenOrientationLockType.h",
      "platform/modules/screen_orientation/WebScreenOrientationType.h",
      "platform/modules/vr/WebVR.h",
      "platform/modules/vr/WebVRClient.h",
      "platform/modules/webusb/WebUSBClient.h",
      "platform/modules/webusb/WebUSBDeviceFilter.h",
      "platform/modules/webusb/WebUSBDevice.h",
      "platform/modules/webusb/WebUSBDeviceInfo.h",
      "platform/modules/webusb/WebUSBDeviceRequestOptions.h",
      "platform/modules/webusb/WebUSBError.h",
      "platform/modules/webusb/WebUSBTransferInfo.h",
      "web/WebAXEnums.h",
      "web/WebAXObject.h",
      "web/WebActiveWheelFlingParameters.h",
      "web/WebArrayBuffer.h",
      "web/WebArrayBufferConverter.h",
      "web/WebArrayBufferView.h",
      "web/WebAutofillClient.h",
      "web/WebBeginFrameArgs.h",
      "web/WebBindings.h",
      "web/WebBlob.h",
      "web/WebCSSParser.h",
      "web/WebCache.h",
      "web/WebColorChooser.h",
      "web/WebColorChooserClient.h",
      "web/WebColorName.h",
      "web/WebColorSuggestion.h",
      "web/WebCompositionUnderline.h",
      "web/WebConsoleMessage.h",
      "web/WebContentDetectionResult.h",
      "web/WebContentSecurityPolicy.h",
      "web/WebContentSettingsClient.h",
      "web/WebContextMenuData.h",
      "web/WebCryptoNormalize.h",
      "web/WebCustomElement.h",
      "web/WebDOMActivityLogger.h",
      "web/WebDOMCustomEvent.h",
      "web/WebDOMError.h",
      "web/WebDOMEvent.h",
      "web/WebDOMFileSystem.h",
      "web/WebDOMMediaStreamTrack.h",
      "web/WebDOMMessageEvent.h",
      "web/WebDOMMouseEvent.h",
      "web/WebDOMProgressEvent.h",
      "web/WebDOMResourceProgressEvent.h",
      "web/WebDataSource.h",
      "web/WebDatabase.h",
      "web/WebDateTimeChooserCompletion.h",
      "web/WebDateTimeChooserParams.h",
      "web/WebDateTimeInputType.h",
      "web/WebDateTimeSuggestion.h",
      "web/WebDevToolsAgent.h",
      "web/WebDevToolsAgentClient.h",
      "web/WebDevToolsFrontend.h",
      "web/WebDevToolsFrontendClient.h",
      "web/WebDeviceEmulationParams.h",
      "web/WebDocument.h",
      "web/WebDocumentType.h",
      "web/WebDragOperation.h",
      "web/WebDragStatus.h",
      "web/WebDraggableRegion.h",
      "web/WebElement.h",
      "web/WebElementCollection.h",
      "web/WebEmbeddedWorker.h",
      "web/WebEmbeddedWorkerStartData.h",
      "web/WebExceptionCode.h",
      "web/WebExternalPopupMenu.h",
      "web/WebExternalPopupMenuClient.h",
      "web/WebFileChooserCompletion.h",
      "web/WebFileChooserParams.h",
      "web/WebFindOptions.h",
      "web/WebFont.h",
      "web/WebFontDescription.h",
      "web/WebFormControlElement.h",
      "web/WebFormElement.h",
      "web/WebFrame.h",
      "web/WebFrameClient.h",
      "web/WebFrameLoadType.h",
      "web/WebFrameWidget.h",
      "web/WebGeolocationClient.h",
      "web/WebGeolocationController.h",
      "web/WebGeolocationError.h",
      "web/WebGeolocationPermissionRequest.h",
      "web/WebGeolocationPermissionRequestManager.h",
      "web/WebGeolocationPosition.h",
      "web/WebGlyphCache.h",
      "web/WebGraphicsContext.h",
      "web/WebHeap.h",
      "web/WebHelperPlugin.h",
      "web/WebHistoryCommitType.h",
      "web/WebHistoryItem.h",
      "web/WebHitTestResult.h",
      "web/WebIconURL.h",
      "web/WebImageCache.h",
      "web/WebImageDecoder.h",
      "web/WebInputElement.h",
      "web/WebInputEvent.h",
      "web/WebKit.h",
      "web/WebLabelElement.h",
      "web/WebLeakDetector.h",
      "web/WebLocalFrame.h",
      "web/WebMIDIClient.h",
      "web/WebMIDIPermissionRequest.h",
      "web/WebMediaDevicesRequest.h",
      "web/WebMediaPlayerAction.h",
      "web/WebMediaStreamRegistry.h",
      "web/WebMemoryUsageInfo.h",
      "web/WebMenuItemInfo.h",
      "web/WebNavigationPolicy.h",
      "web/WebNavigationType.h",
      "web/WebNavigatorContentUtilsClient.h",
      "web/WebNetworkStateNotifier.h",
      "web/WebNode.h",
      "web/WebNodeList.h",
      "web/WebOptionElement.h",
      "web/WebPagePopup.h",
      "web/WebPageSerializer.h",
      "web/WebPageSerializerClient.h",
      "web/WebPerformance.h",
      "web/WebPlugin.h",
      "web/WebPluginAction.h",
      "web/WebPluginContainer.h",
      "web/WebPluginDocument.h",
      "web/WebPluginParams.h",
      "web/WebPluginScriptForbiddenScope.h",
      "web/WebPopupMenuInfo.h",
      "web/WebPopupType.h",
      "web/WebPrerendererClient.h",
      "web/WebPrintParams.h",
      "web/WebPrintPresetOptions.h",
      "web/WebPrintScalingOption.h",
      "web/WebRange.h",
      "web/WebRemoteFrame.h",
      "web/WebRemoteFrameClient.h",
      "web/WebRuntimeFeatures.h",
      "web/WebSandboxFlags.h",
      "web/WebScopedMicrotaskSuppression.h",
      "web/WebScopedUserGesture.h",
      "web/WebScopedWindowFocusAllowedIndicator.h",
      "web/WebScriptBindings.h",
      "web/WebScriptController.h",
      "web/WebScriptExecutionCallback.h",
      "web/WebScriptSource.h",
      "web/WebSearchableFormData.h",
      "web/WebSecurityOrigin.h",
      "web/WebSecurityPolicy.h",
      "web/WebSelectElement.h",
      "web/WebSelection.h",
      "web/WebSelector.h",
      "web/WebSerializedScriptValue.h",
      "web/WebSerializedScriptValueVersion.h",
      "web/WebServiceWorkerContextClient.h",
      "web/WebServiceWorkerContextProxy.h",
      "web/WebServiceWorkerNetworkProvider.h",
      "web/WebSettings.h",
      "web/WebSharedWorker.h",
      "web/WebSharedWorkerClient.h",
      "web/WebSharedWorkerConnector.h",
      "web/WebSharedWorkerRepositoryClient.h",
      "web/WebSocket.h",
      "web/WebSocketClient.h",
      "web/WebSpeechGrammar.h",
      "web/WebSpeechRecognitionHandle.h",
      "web/WebSpeechRecognitionParams.h",
      "web/WebSpeechRecognitionResult.h",
      "web/WebSpeechRecognizer.h",
      "web/WebSpeechRecognizerClient.h",
      "web/WebSpellCheckClient.h",
      "web/WebStorageEventDispatcher.h",
      "web/WebSurroundingText.h",
      "web/WebTestInterfaceFactory.h",
      "web/WebTestingSupport.h",
      "web/WebTextAffinity.h",
      "web/WebTextAreaElement.h",
      "web/WebTextCheckingCompletion.h",
      "web/WebTextCheckingResult.h",
      "web/WebTextCheckingType.h",
      "web/WebTextDecorationType.h",
      "web/WebTextDirection.h",
      "web/WebTextInputInfo.h",
      "web/WebTextInputType.h",
      "web/WebTextRun.h",
      "web/WebTouchAction.h",
      "web/WebTouchPoint.h",
      "web/WebTreeScopeType.h",
      "web/WebURLLoaderOptions.h",
      "web/WebUserGestureIndicator.h",
      "web/WebUserGestureToken.h",
      "web/WebUserMediaClient.h",
      "web/WebUserMediaRequest.h",
      "web/WebView.h",
      "web/WebViewClient.h",
      "web/WebWidget.h",
      "web/WebWidgetClient.h",
      "web/WebWindowFeatures.h",
      "web/WebWorkerContentSettingsClientProxy.h",
      "web/default/WebRenderTheme.h",
      "web/linux/WebFontRendering.h",
      "web/mac/WebScrollbarTheme.h",
      "web/mac/WebSubstringUtil.h",
      "web/modules/notifications/WebNotificationPermissionCallback.h",
      "web/win/WebFontRendering.h",
    ],
  },
}
