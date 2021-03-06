//
//  GraphView.swift
//  Correctable-Pronunciation
//
//  Created by 차요셉 on 2020. 12. 15..
//  Copyright © 2020 차요셉. All rights reserved.
//

import UIKit

@IBDesignable class WeekView: UIView {
    var label: UILabel!
    var graphPoints = [0,0,0,0,0,0,0]
    private struct Constants {
        static let cornerRadiusSize = CGSize(width: 8.0, height: 8.0)
        static let margin: CGFloat = 20.0
        static let topBorder: CGFloat = 60
        static let bottomBorder: CGFloat = 50
        static let colorAlpha: CGFloat = 0.3
        static let circleDiameter: CGFloat = 5.0
    }
    // 1. 그래디언트 프로퍼티: IBInspectable이므로 storyboard에서 변경 가능
    @IBInspectable var startColor: UIColor = .red
    @IBInspectable var endColor: UIColor = .green
    override func draw(_ rect: CGRect) {
        self.subviews.forEach({
                                switch $0.tag {
                                case 0 ..< graphPoints.count:
                                    $0.removeFromSuperview()
                                default:
                                    return
                                }
        })
        let width = rect.width
        let height = rect.height
        let path = UIBezierPath(roundedRect: rect, byRoundingCorners: .allCorners, cornerRadii: Constants.cornerRadiusSize)
        path.addClip()
        let context = UIGraphicsGetCurrentContext()!
        let colors = [startColor.cgColor, endColor.cgColor]
        
        // 3. 컬라스페이스 (CMYK, greyscale, RGB 중에서 선택)
        let colorSpace = CGColorSpaceCreateDeviceRGB()
        
        // 4. 그래디언트를 위한 컬러 변경 위치
        let colorLocations: [CGFloat] = [0.0, 1.0]
        
        // 5. 그래디언트 생성
        let gradient = CGGradient(colorsSpace: colorSpace, colors: colors as CFArray, locations: colorLocations)!
        
        // 6. 그래디언트 드로잉
        let startPoint = CGPoint.zero
        let endPoint = CGPoint(x: 0, y: bounds.height)
        context.drawLinearGradient(gradient, start: startPoint, end: endPoint, options: [])
        
        let margin = Constants.margin
        let graphWidth = width - margin * 2 - 4
        let columnXPoint = { (column: Int) -> CGFloat in
            let spacing = graphWidth / CGFloat(self.graphPoints.count - 1)
            return CGFloat(column) * spacing + margin + 2
            
        }
        
        let topBorder = Constants.topBorder
        let bottomBorder = Constants.bottomBorder
        let graphHeight = height - topBorder - bottomBorder
        let maxValue = 100
        let columnYPoint = { (graphPoint: Int) -> CGFloat in
            let y = CGFloat(graphPoint) / CGFloat(maxValue) * graphHeight
            return graphHeight + topBorder - y
        }
        UIColor.white.setFill()
        UIColor.white.setStroke()
        
        let graphPath = UIBezierPath()
        graphPath.move(to: CGPoint(x: columnXPoint(0), y: columnYPoint(graphPoints[0])))
        
        for i in 1..<graphPoints.count {
            let nextPoint = CGPoint(x: columnXPoint(i), y: columnYPoint(graphPoints[i]))
            graphPath.addLine(to: nextPoint)
        }
        graphPath.stroke()
        
        for i in 0..<graphPoints.count {
            var point = CGPoint(x: columnXPoint(i), y: columnYPoint(graphPoints[i]))
            point.x -= Constants.circleDiameter / 2
            point.y -= Constants.circleDiameter / 2
            if graphPoints[i] > 0 {
                label = UILabel(frame: CGRect(x: columnXPoint(i) - 10, y: columnYPoint(graphPoints[i]) - 20, width: 20, height: 20))
                label.text = "\(graphPoints[i])"
                label.font = UIFont(name: "AppleSDGothicNeo-Light", size: 15)
                label.textColor = .white
                label.textAlignment = .center
                label.adjustsFontSizeToFitWidth = true
                label.tag = i
                addSubview(label)
            }
            
            let circle = UIBezierPath(ovalIn: CGRect(origin: point, size: CGSize(width: Constants.circleDiameter, height: Constants.circleDiameter)))
            circle.fill()
        }
        
        let linePath = UIBezierPath()
        
        linePath.move(to: CGPoint(x:margin, y: topBorder))
        linePath.addLine(to: CGPoint(x: width - margin, y: topBorder))
        
        linePath.move(to: CGPoint(x: margin, y: graphHeight/2 + topBorder))
        linePath.addLine(to: CGPoint(x:width - margin, y: graphHeight/2 + topBorder))
        
        linePath.move(to: CGPoint(x: margin, y: height - bottomBorder))
        linePath.addLine(to: CGPoint(x: width - margin, y: height - bottomBorder))
        let color = UIColor(white: 1.0, alpha: Constants.colorAlpha)
        color.setStroke()
        linePath.lineWidth = 1.0
        linePath.stroke()
        
    }
}
