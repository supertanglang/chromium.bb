// Copyright 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// This file has been auto-generated by {{code_generator}}. DO NOT MODIFY!

#ifndef {{v8_class}}_h
#define {{v8_class}}_h

{% for filename in header_includes %}
#include "{{filename}}"
{% endfor %}

namespace blink {

class ExceptionState;

class {{v8_class}} {
public:
    static {{cpp_class}}* toImpl(v8::Isolate*, v8::Handle<v8::Value>, ExceptionState&);
};

v8::Handle<v8::Value> toV8({{cpp_class}}*, v8::Handle<v8::Object>, v8::Isolate*);

template<class CallbackInfo>
inline void v8SetReturnValue(const CallbackInfo& callbackInfo, {{cpp_class}}* impl)
{
    v8SetReturnValue(callbackInfo, toV8(impl, callbackInfo.Holder(), callbackInfo.GetIsolate()));
}

} // namespace blink

#endif // {{v8_class}}_h
