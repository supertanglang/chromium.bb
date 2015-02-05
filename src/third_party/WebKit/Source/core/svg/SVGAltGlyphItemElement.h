/*
 * Copyright (C) 2011 Leo Yang <leoyang@webkit.org>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Library General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Library General Public License for more details.
 *
 * You should have received a copy of the GNU Library General Public License
 * along with this library; see the file COPYING.LIB.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
 * Boston, MA 02110-1301, USA.
 */

#ifndef SVGAltGlyphItemElement_h
#define SVGAltGlyphItemElement_h

#if ENABLE(SVG_FONTS)
#include "core/SVGNames.h"
#include "core/svg/SVGElement.h"
#include "wtf/Vector.h"

namespace blink {

class SVGAltGlyphItemElement FINAL : public SVGElement {
    DEFINE_WRAPPERTYPEINFO();
public:
    DECLARE_NODE_FACTORY(SVGAltGlyphItemElement);

    bool hasValidGlyphElements(Vector<AtomicString>& glyphNames) const;

private:
    explicit SVGAltGlyphItemElement(Document&);

    virtual bool rendererIsNeeded(const RenderStyle&) OVERRIDE { return false; }
};

} // namespace blink

#endif // ENABLE(SVG_FONTS)
#endif // SVGAltGlyphItemElement_h
